<script>
	import axios from 'axios';
	import { writable } from 'svelte/store';
	import Papa from 'papaparse';

	export let filePath1;

	let openimg = false;
	let showCsv = false;
	let showHdf5Datasets = false;

	let imageUrl = '';
	let csvData = writable([]);
	let currentData = writable([]);
	let datasets = writable([]);
	let datasetToConvert = '';
	let datasetRows = writable([]); // แบ่ง dataset เป็นแถวละ 5 รายการ
	let currentPage = 1;
	let rowsPerPage = 20;
	let visibleRows = 2; // จำนวนเริ่มต้นในการแสดงแถว datasets

	const handleFileClick = async (filePath) => {
		try {
			const fileExtension = filePath.split('.').pop().toLowerCase();

			switch (fileExtension) {
				case 'jpg':
				case 'jpeg':
					openimg = true;
					showCsv = false;
					showHdf5Datasets = false;

					const imageResponse = await axios.get(
						`http://localhost:3211/read-jpg?file=${encodeURIComponent(filePath)}`,
						{ responseType: 'blob' }
					);
					imageUrl = URL.createObjectURL(new Blob([imageResponse.data]));
					break;

				case 'csv':
					openimg = false;
					showCsv = true;
					showHdf5Datasets = false;

					const csvResponse = await axios.get(`http://localhost:3211/read-csv?file=${filePath}`);
					Papa.parse(csvResponse.data, {
						header: true,
						complete: (result) => {
							csvData.set(result.data);
							loadCurrentPageData();
						},
						error: (error) => {
							console.error('Error parsing CSV:', error);
						}
					});
					break;

				case 'hdf5':
					openimg = false;
					showCsv = false;
					showHdf5Datasets = true;

					const hdf5Response = await axios.get(
						`http://localhost:8000/datasets?filename=${filePath}`
					);
					datasets.set(hdf5Response.data.available_datasets);
					groupDatasetsIntoRows(hdf5Response.data.available_datasets);
					break;

				default:
					openimg = false;
					showCsv = false;
					showHdf5Datasets = false;
					console.warn('Unsupported file type:', fileExtension);
			}
		} catch (error) {
			console.error('Error handling file click:', error);
		}
	};

	// ฟังก์ชันจัดกลุ่ม datasets เป็นแถวละ 5
	const groupDatasetsIntoRows = (datasetsList) => {
		const rows = [];
		for (let i = 0; i < datasetsList.length; i += 5) {
			rows.push(datasetsList.slice(i, i + 5));
		}
		datasetRows.set(rows);
	};

	const loadMoreRows = () => {
		visibleRows += 2; // เพิ่มแถวละ 2 ทุกครั้งที่กดปุ่ม More
	};

	const loadCurrentPageData = () => {
		csvData.subscribe((data) => {
			const start = (currentPage - 1) * rowsPerPage;
			const end = start + rowsPerPage;
			currentData.set(data.slice(start, end));
		});
	};

	const nextPage = () => {
		currentPage += 1;
		loadCurrentPageData();
	};

	const prevPage = () => {
		if (currentPage > 1) {
			currentPage -= 1;
			loadCurrentPageData();
		}
	};

	const convertToJpg = async () => {
		try {
			const response = await axios.post('http://localhost:8000/convert_to_jpg', {
				filename: filePath1, // ใช้ชื่อไฟล์ HDF5
				datasetNames: [datasetToConvert] // ใช้ชื่อ dataset ที่ต้องการแปลง
			});
			console.log('Conversion result:', response.data);
			location.reload();
		} catch (error) {
			console.error('Error converting datasets:', error.response ? error.response.data : error);
		}
	};

	const convertd = (dataset) => {
		datasetToConvert = dataset;
		convertToJpg();
	};

	$: if (filePath1) {
		handleFileClick(filePath1);
	}
</script>

<div class="border w-full border-black mx-4 mr-20">
	{#if filePath1}
		<div class="flex justify-center my-2">
			<p>Selected file: {filePath1}</p>
		</div>
	{/if}

	<!-- Show image if JPG is selected -->
	{#if openimg}
		<div class="flex justify-center my-10">
			<img src={imageUrl} alt="Selected Image" class="image" />
		</div>
	{/if}

	<!-- Show CSV data if CSV is selected -->
	{#if showCsv}
		<div class="overflow-scroll w-[60rem]" style="max-height: 400px; overflow-y: auto;">
			<table class="table-auto border-collapse border border-gray-400">
				<thead>
					<tr>
						{#each Object.keys($currentData[0] || {}) as header}
							<th class="border border-gray-400">{header}</th>
						{/each}
					</tr>
				</thead>
				<tbody>
					{#each $currentData as row}
						<tr>
							{#each Object.values(row) as value}
								<td class="border text-center px-2 border-gray-400">{value}</td>
							{/each}
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
		<div class="flex justify-between mt-4">
			<button on:click={prevPage} disabled={currentPage === 1} class="border px-4 py-2"
				>Previous</button
			>
			<button on:click={nextPage} class="border px-4 py-2">Next</button>
		</div>
	{/if}

	<!-- Show HDF5 datasets if HDF5 file is selected -->
	{#if showHdf5Datasets}
		<div class="mt-4">
			<h2 class="ml-5">Available Datasets:</h2>
			<table class="table-auto flex justify-center overflow-y-auto max-h-64">
				<tbody>
					{#each $datasetRows.slice(0, visibleRows) as row}
						<tr>
							{#each row as dataset}
								<td
									on:click={() => convertd(dataset)}
									class="px-4 py-2 cursor-pointer hover:bg-gray-200"
								>
									{dataset}
								</td>
							{/each}
						</tr>
					{/each}
				</tbody>
			</table>
			{#if $datasetRows.length > visibleRows}
				<div class="flex justify-center">
					<button on:click={loadMoreRows} class=" border px-4 py-2">More</button>
				</div>
			{/if}
		</div>
	{/if}
</div>

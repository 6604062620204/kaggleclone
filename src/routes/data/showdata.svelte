<script>
	//@ts-nocheck
	import { onMount } from 'svelte';
	import axios from 'axios';
	import { writable } from 'svelte/store';
	import Rendertree from '../../components/rendertree.svelte';

	const files = writable([]); // กำหนดค่าเริ่มต้นเป็น array เปล่า
	const csvData = writable([]);
	console.log(csvData);
	const openFolders = writable({});

	onMount(async () => {
		await fetchFileTree();
	});

	export const fetchFileTree = async () => {
		try {
			const response = await axios.get('http://localhost:3211/list-files');
			files.set(response.data);
			// console.log(response.data);
		} catch (error) {
			console.error('Error fetching file tree:', error);
		}
	};
</script>

<div class="flex justify-between">
	<div class="">
		{#if $csvData.length > 0}
			<!-- แสดงข้อมูล CSV -->
			<table class="w-full border-collapse">
				<thead>
					<tr>
						{#each Object.keys($csvData[0]) as header}
							<th class="border p-2">{header}</th>
						{/each}
					</tr>
				</thead>
				<tbody>
					{#each $csvData as row}
						<tr>
							{#each Object.values(row) as cell}
								<td class="border p-2">{cell}</td>
							{/each}
						</tr>
					{/each}
				</tbody>
			</table>
		{/if}
	</div>

	<!-- ตรวจสอบว่า files มีข้อมูลก่อนที่จะส่งไปที่ Rendertree component -->
	{#if $files.length > 0}
		<Rendertree treeData={$files} />
	{:else}
		<p>กำลังโหลดข้อมูลไฟล์...</p>
	{/if}
</div>

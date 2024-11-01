<script>
	let open = false;

	function toggles() {
		open = !open;
	}
</script>

<div class="flex">
	<!-- Sidebar Section -->
	{#if !open}
		<div class="fixed top-0 left-0 h-full w-64 bg-base-200 shadow-lg border-r z-50">
			<ul class="menu bg-base-200 text-base-content min-h-full w-64">
				<div class="flex">
					<button on:click={toggles}
						><img src="/assets/image/menu.svg" class=" h-8 rounded-md mr-4" alt="" /></button
					>

					<img src="/assets/image/site-logo.svg" class="w-24" alt="" />
				</div>
				<div class="pt-6 pb-4">
					<a href="/" class="flex border-2 rounded-full w-fit drop-shadow-2xl px-4 py-1">
						<svg
							class=""
							width="36"
							height="36"
							viewBox="0 0 36 36"
							fill="none"
							xmlns="http://www.w3.org/2000/svg"
							style="flex-shrink: 0;"
							><path
								fill-rule="evenodd"
								clip-rule="evenodd"
								d="M20 30L20 16L16 20L16 30L20 30Z"
								fill="#20BEFF"
							></path><path
								fill-rule="evenodd"
								clip-rule="evenodd"
								d="M20 20L30 20L30 16L20 16L20 20Z"
								fill="#20BEFF"
							></path><path
								fill-rule="evenodd"
								clip-rule="evenodd"
								d="M16 20L20 16L15.937 16L6 16L6 20L16 20Z"
								fill="#20BEFF"
							></path><rect
								x="20"
								y="16"
								width="4"
								height="10"
								transform="rotate(-180 20 16)"
								fill="#20BEFF"
							></rect></svg
						>
						<p class="text-lg p-1 pl-4">Create</p>
					</a>
				</div>
				<!-- Sidebar content here -->
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/home.svg" class="w-6" alt="" /><a class="">Home</a>
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/cup.svg" class="w-6" alt="" /><a>Competitions</a>
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/data.svg" class="w-6" alt="" /><a>Datasets</a>
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/model.svg" class="w-6" alt="" /> <a>Models</a>
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/code.svg" class="w-6" alt="" /> <a>Code</a>
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/chat.svg" class="w-6" alt="" /><a>Discussions</a>
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/learn.svg" class="w-6" alt="" /><a>Learn</a>
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<!-- svelte-ignore a11y-missing-attribute -->
						<img src="/assets/image/arrow.svg" class="w-6" alt="" /><a>More</a>
					</div>
				</li>
				<hr class="my-5 stroke-2" />
				<li>
					<div class="flex gap-6">
						<!-- svelte-ignore a11y-missing-attribute -->
						<img src="/assets/image/note.svg" class="w-6" alt="" /><a>Your work</a>
					</div>
				</li>
			</ul>
		</div>
		<div class="ml-64 p-6 w-full z-0">
			<!-- Main content goes here -->
			<label class="input input-bordered border-gray-400 rounded-full flex items-center gap-2">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 16 16"
					fill="currentColor"
					class="h-4 w-4 opacity-70"
				>
					<path
						fill-rule="evenodd"
						d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
						clip-rule="evenodd"
					/>
				</svg>
				<input type="text" class="grow" placeholder="Search" />
			</label>
			<div class="flex justify-between mt-3">
				<div class="flex">
					<img src="/assets/image/thumbnail1.png" class="h-8" alt="" />
					<p class="text-sm mt-2 ml-4 text-gray-600">
						International Skin Imaging Collaboration (ISIC) · Research Code Competition · a month
						ago
					</p>
				</div>
				<div class="flex">
					<button class="btn btn-primary bg-black text-white rounded-full p-0 px-6 hover:bg-black"
						>Late Submission</button
					>

					<!-- circle button ...  -->
					<img src="/assets/image/dot.svg" class="w-6 mx-4" alt="" />
				</div>
			</div>
			<div class="flex justify-between mt-10">
				<div>
					<p class="text-4xl font-bold mt-5">ISIC 2024 - Skin Cancer Detection with 3D-TBP</p>
					<p class="text-gray-500">
						Identify cancers among skin lesions cropped from 3D total body photographs
					</p>
				</div>
				<img src="/assets/image/header.png" class="w-72 mr-10 rounded-lg" alt="" />
			</div>

			<div class="p-1 mt-4 flex relative">
				<div class="absolute inset-x-0 bottom-0 w-full">
					<div class="h-0.5 w-[100%] bg-gray-300"></div>
				</div>
				<a href="/"><button class="btn btn-ghost">Overview</button></a>
				<a href="data"><button class="btn btn-ghost">Data</button></a>
			</div>
			<hr />
		</div>
	{/if}
	{#if open}
		<div class="fixed top-0 left-0 h-full w-20 bg-base-200 shadow-lg border-r z-50">
			<ul class="menu bg-base-200 text-base-content min-h-full w-20">
				<div class="flex">
					<button on:click={toggles}
						><img
							src="/assets/image/menu.svg"
							class="mx-4 my-2 h-8 rounded-md mr-4"
							alt=""
						/></button
					>
				</div>
				<div class="pt-6 pb-4">
					<a href="/" class="flex justify-center p-2 border-2 rounded-full drop-shadow-2xl">
						<svg
							class=""
							width="36"
							height="36"
							viewBox="0 0 36 36"
							fill="none"
							xmlns="http://www.w3.org/2000/svg"
							style="flex-shrink: 0;"
							><path
								fill-rule="evenodd"
								clip-rule="evenodd"
								d="M20 30L20 16L16 20L16 30L20 30Z"
								fill="#20BEFF"
							></path><path
								fill-rule="evenodd"
								clip-rule="evenodd"
								d="M20 20L30 20L30 16L20 16L20 20Z"
								fill="#20BEFF"
							></path><path
								fill-rule="evenodd"
								clip-rule="evenodd"
								d="M16 20L20 16L15.937 16L6 16L6 20L16 20Z"
								fill="#20BEFF"
							></path><rect
								x="20"
								y="16"
								width="4"
								height="10"
								transform="rotate(-180 20 16)"
								fill="#20BEFF"
							></rect></svg
						>
					</a>
				</div>
				<!-- Sidebar content here -->
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/home.svg" class="w-6" alt="" />
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/cup.svg" class="w-6" alt="" />
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/data.svg" class="w-6" alt="" />
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/model.svg" class="w-6" alt="" />
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/code.svg" class="w-6" alt="" />
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/chat.svg" class="w-6" alt="" />
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/learn.svg" class="w-6" alt="" />
					</div>
				</li>
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/arrow.svg" class="w-6" alt="" />
					</div>
				</li>
				<hr class="my-5" />
				<li>
					<div class="flex gap-6">
						<img src="/assets/image/note.svg" class="w-6" alt="" />
					</div>
				</li>
			</ul>
		</div>
		<div class="ml-20 p-6 w-full z-0">
			<!-- Main content goes here -->
			<label class="input input-bordered border-gray-400 rounded-full flex items-center gap-2">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 16 16"
					fill="currentColor"
					class="h-4 w-4 opacity-70"
				>
					<path
						fill-rule="evenodd"
						d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z"
						clip-rule="evenodd"
					/>
				</svg>
				<input type="text" class="grow" placeholder="Search" />
			</label>
			<div class="flex justify-between mt-3">
				<div class="flex">
					<img src="/assets/image/thumbnail1.png" class="h-8" alt="" />
					<p class="text-sm mt-2 ml-4 text-gray-600">
						International Skin Imaging Collaboration (ISIC) · Research Code Competition · a month
						ago
					</p>
				</div>
				<div class="flex">
					<button class="btn btn-primary bg-black text-white rounded-full p-0 px-6 hover:bg-black"
						>Late Submission</button
					>

					<!-- circle button ...  -->
					<img src="/assets/image/dot.svg" class="w-6 mx-4" alt="" />
				</div>
			</div>
			<div class="flex justify-between mt-10">
				<div>
					<p class="text-4xl font-bold mt-5">ISIC 2024 - Skin Cancer Detection with 3D-TBP</p>
					<p class="text-gray-500">
						Identify cancers among skin lesions cropped from 3D total body photographs
					</p>
				</div>
				<img src="/assets/image/header.png" class="w-72 mr-10 rounded-lg" alt="" />
			</div>

			<div class="p-1 mt-4 flex relative">
				<div class="absolute inset-x-0 bottom-0 w-full">
					<div class="h-0.5 w-[100%] bg-gray-300"></div>
				</div>
				<a href="/"><button class="btn btn-ghost">Overview</button></a>
				<a href="data"><button class="btn btn-ghost">Data</button></a>
			</div>
			<hr />
		</div>
	{/if}
</div>

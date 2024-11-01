<script>
	import { writable } from 'svelte/store';
	import Datasvelte from './datasvelte.svelte';

	export let treeData = [];
	let filePath1 = 'ยังไม่ได้เลือกไฟล์';
	let boolpath = false;
	const openFolders = writable({});
	const visibleItemsCount = writable({});

	function handleFileClick(filePath) {
		boolpath = true;
		//console.log('File clicked:', filePath);
		filePath1 = filePath;
	}

	function toggleFolder(folderPath) {
		openFolders.update((open) => ({
			...open,
			[folderPath]: !open[folderPath]
		}));

		visibleItemsCount.update((count) => {
			if (!count[folderPath]) {
				return { ...count, [folderPath]: 10 };
			}
			return count;
		});
	}

	function showMoreItems(folderPath, totalItems) {
		visibleItemsCount.update((count) => ({
			...count,
			[folderPath]: Math.min(totalItems, count[folderPath] + 10)
		}));
	}

	function getVisibleItems(folderPath, items) {
		let count = $visibleItemsCount[folderPath] || 10;
		return items.slice(0, count);
	}
</script>

<div
	class="flex justify-between w-full
"
>
	<Datasvelte {filePath1} />

	<ul>
		{#each treeData as item (item.name)}
			{#if item.type === 'folder'}
				<li>
					<div class="folder">
						<span class="font-bold cursor-pointer" on:click={() => toggleFolder(item.name)}>
							{item.name}
						</span>
					</div>
					{#if $openFolders[item.name]}
						<ul class="folder-contents ml-4">
							{#each getVisibleItems(item.name, item.contents) as subItem}
								<li>
									{#if subItem.type === 'folder'}
										<div class="folder">
											<span
												class="font-bold cursor-pointer"
												on:click={() => toggleFolder(item.name + '/' + subItem.name)}
											>
												{subItem.name}
											</span>
										</div>
										<!-- แสดงเนื้อหาใน subFolder -->
										{#if $openFolders[item.name + '/' + subItem.name]}
											<ul class="folder-contents ml-4">
												{#each getVisibleItems(item.name + '/' + subItem.name, subItem.contents) as subSubItem}
													<li>
														{#if subSubItem.type === 'folder'}
															<div class="folder">
																<span
																	class="font-bold cursor-pointer"
																	on:click={() =>
																		toggleFolder(
																			item.name + '/' + subItem.name + '/' + subSubItem.name
																		)}
																>
																	{subSubItem.name}
																</span>
															</div>
														{/if}
														{#if subSubItem.type === 'file'}
															<div
																class="file cursor-pointer"
																on:click={() =>
																	handleFileClick(
																		item.name + '/' + subItem.name + '/' + subSubItem.name
																	)}
															>
																{subSubItem.name}
															</div>
														{/if}
													</li>
												{/each}
												{#if subItem.contents.length > $visibleItemsCount[item.name + '/' + subItem.name]}
													<li>
														<button
															on:click={() =>
																showMoreItems(
																	item.name + '/' + subItem.name,
																	subItem.contents.length
																)}
														>
															Show More
														</button>
													</li>
												{/if}
											</ul>
										{/if}
									{/if}
									{#if subItem.type === 'file'}
										<div
											class="file cursor-pointer"
											on:click={() => handleFileClick(item.name + '/' + subItem.name)}
										>
											{subItem.name}
										</div>
									{/if}
								</li>
							{/each}
							{#if item.contents.length > $visibleItemsCount[item.name]}
								<li>
									<button on:click={() => showMoreItems(item.name, item.contents.length)}>
										<p class="text-gray-500">Show More</p>
									</button>
								</li>
							{/if}
						</ul>
					{/if}
				</li>
			{/if}

			{#if item.type === 'file'}
				<li>
					<div class="file cursor-pointer" on:click={() => handleFileClick(item.name)}>
						{item.name}
					</div>
				</li>
			{/if}
		{/each}
	</ul>
</div>

<style>
	.folder-contents {
		max-height: 200px;
		overflow-y: auto;
	}
</style>

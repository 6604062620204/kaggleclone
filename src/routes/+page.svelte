<script>
	import { onMount } from 'svelte';

	let open = false;

	function toggles() {
		open = !open;
	}
</script>

{#if !open}
	<div class="ml-64 p-6 z-0">
		<div class="flex justify-between">
			<div class="flex">
				<div class="flex flex-col text-gray-600 mr-10">
					<p class="text-2xl font-bold text-black">Overview</p>
					<br />
					<p>
						In this competition, you'll develop image-based algorithms to identify histologically
						confirmed skin cancer cases with single-lesion crops from 3D total body photos (TBP).
						The image quality resembles close-up smartphone photos, which are regularly submitted
						for telehealth purposes. Your binary classification algorithm could be used in settings
						without access to specialized care and improve triage for early skin cancer detection.
					</p>
					<img src="/assets/image/overviewline.png" alt="" />
					<br />
					<hr />
					<div class="collapse collapse-arrow bg-base-200">
						<input type="checkbox" />
						<div class="collapse-title text-xl font-medium text-black">Description</div>
						<div class="collapse-content">
							<p>
								Skin cancer can be deadly if not caught early, but many populations lack specialized
								dermatologic care. Over the past several years, dermoscopy-based AI algorithms have
								been shown to benefit clinicians in diagnosing melanoma, basal cell, and squamous
								cell carcinoma. However, determining which individuals should see a clinician in the
								first place has great potential impact. Triaging applications have a significant
								potential to benefit underserved populations and improve early skin cancer
								detection, the key factor in long-term patient outcomes.
							</p>
							<br />
							<p>
								Dermatoscope images reveal morphologic features not visible to the naked eye, but
								these images are typically only captured in dermatology clinics. Algorithms that
								benefit people in primary care or non-clinical settings must be adept to evaluating
								lower quality images. This competition leverages 3D TBP to present a novel dataset
								of every single lesion from thousands of patients across three continents with
								images resembling cell phone photos.
							</p>
							<br />
							<p>
								This competition challenges you to develop AI algorithms that differentiate
								histologically-confirmed malignant skin lesions from benign lesions on a patient.
								Your work will help to improve early diagnosis and disease prognosis by extending
								the benefits of automated skin cancer detection to a broader population and
								settings.
							</p>
						</div>
					</div>
					<hr />
					<div class="collapse collapse-arrow bg-base-200">
						<input type="checkbox" />
						<div class="collapse-title text-xl font-medium text-black">Evaluation</div>
						<div class="collapse-content">
							<p class="font-medium text-black">Primary Scoring Metric</p>
						</div>
					</div>
				</div>
			</div>
			<div class="flex flex-col gap-4 ml-10 w-full">
				<div>
					<p>Files</p>
					<p class="text-gray-500">401064 file</p>
				</div>
				<div>
					<p>Size</p>
					<p class="text-gray-500">2.69 GB</p>
				</div>
				<div>
					<p>Type</p>
					<p class="text-gray-500">jpg, csv, hdf5</p>
				</div>
				<div>
					<p>License</p>
					<a href="https://creativecommons.org/licenses/by-nc/4.0/" class="text-gray-500 underline"
						>Attribution-NonCommercial 4.0 Inter</a
					>
				</div>
			</div>
		</div>
	</div>
{/if}
{#if open}
	<div class="ml-20 p-6 z-0">
		<div class="flex justify-between">
			<div class="flex">
				<div class="flex flex-col text-gray-600 mr-10">
					<p class="text-2xl font-bold text-black">Overview</p>
					<br />
					<p>
						In this competition, you'll develop image-based algorithms to identify histologically
						confirmed skin cancer cases with single-lesion crops from 3D total body photos (TBP).
						The image quality resembles close-up smartphone photos, which are regularly submitted
						for telehealth purposes. Your binary classification algorithm could be used in settings
						without access to specialized care and improve triage for early skin cancer detection.
					</p>
					<img src="/assets/image/overviewline.png" alt="" />
					<br />
					<hr />
					<div class="collapse collapse-arrow bg-base-200">
						<input type="checkbox" />
						<div class="collapse-title text-xl font-medium text-black">Description</div>
						<div class="collapse-content">
							<p>
								Skin cancer can be deadly if not caught early, but many populations lack specialized
								dermatologic care. Over the past several years, dermoscopy-based AI algorithms have
								been shown to benefit clinicians in diagnosing melanoma, basal cell, and squamous
								cell carcinoma. However, determining which individuals should see a clinician in the
								first place has great potential impact. Triaging applications have a significant
								potential to benefit underserved populations and improve early skin cancer
								detection, the key factor in long-term patient outcomes.
							</p>
							<br />
							<p>
								Dermatoscope images reveal morphologic features not visible to the naked eye, but
								these images are typically only captured in dermatology clinics. Algorithms that
								benefit people in primary care or non-clinical settings must be adept to evaluating
								lower quality images. This competition leverages 3D TBP to present a novel dataset
								of every single lesion from thousands of patients across three continents with
								images resembling cell phone photos.
							</p>
							<br />
							<p>
								This competition challenges you to develop AI algorithms that differentiate
								histologically-confirmed malignant skin lesions from benign lesions on a patient.
								Your work will help to improve early diagnosis and disease prognosis by extending
								the benefits of automated skin cancer detection to a broader population and
								settings.
							</p>
						</div>
					</div>
					<hr />
					<div class="collapse collapse-arrow bg-base-200">
						<input type="checkbox" />
						<div class="collapse-title text-xl font-medium text-black">Evaluation</div>
						<div class="collapse-content">
							<p class="font-medium text-black">Primary Scoring Metric</p>
						</div>
					</div>
				</div>
			</div>
			<div class="flex flex-col gap-4 ml-10 w-full">
				<div>
					<p>Files</p>
					<p class="text-gray-500">401064 file</p>
				</div>
				<div>
					<p>Size</p>
					<p class="text-gray-500">2.69 GB</p>
				</div>
				<div>
					<p>Type</p>
					<p class="text-gray-500">jpg, csv, hdf5</p>
				</div>
				<div>
					<p>License</p>
					<a href="https://creativecommons.org/licenses/by-nc/4.0/" class="text-gray-500 underline"
						>Attribution-NonCommercial 4.0 Inter</a
					>
				</div>
			</div>
		</div>
	</div>
{/if}

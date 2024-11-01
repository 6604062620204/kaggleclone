<script>
	import Showdata from './showdata.svelte';
</script>

<div class="ml-64 p-6 z-0">
	<div class="flex justify-between">
		<div class="flex">
			<div class="flex flex-col text-gray-600 mr-10">
				<p class="text-2xl font-bold text-black">Dataset Description</p>
				<br />
				<p class="font-semibold text-gray-700 my-2">What should I expect the data format to be?</p>
				<p>
					The dataset consists of diagnostically labelled images with additional metadata. The
					images are JPEGs. The associated .csv file contains a binary diagnostic label (<span
						class="bg-gray-100">target</span
					>), potential input variables (e.g. <span class="bg-gray-100">age_approx</span>,
					<span class="bg-gray-100">sex</span>,
					<span class="bg-gray-100">anatom_site_general</span>, etc.), and additional attributes
					(e.g. image source and precise diagnosis).
				</p>
				<p class="font-semibold text-gray-700 my-2">What am I predicting?</p>
				<p>
					In this challenge you are differentiating benign from malignant cases. For each image (<span
						class="bg-gray-100">isic_id</span
					>) you are assigning the probability (<span class="bg-gray-100">target</span>) ranging [0,
					1] that the case is malignant.
				</p>
				<p class="font-semibold text-xl text-black my-2">
					The SLICE-3D dataset - skin lesion image crops extracted from 3D TBP for skin cancer
					detection
				</p>
				<p>
					To mimic non-dermoscopic images, this competition uses standardized cropped lesion-images
					of lesions from 3D Total Body Photography (TBP). Vectra WB360, a 3D TBP product from
					Canfield Scientific, captures the complete visible cutaneous surface area in one
					macro-quality resolution tomographic image. An AI-based software then identifies
					individual lesions on a given 3D capture. This allows for the image capture and
					identification of all lesions on a patient, which are exported as individual 15x15 mm
					field-of-view cropped photos. The dataset contains every lesion from a subset of thousands
					of patients seen between the years 2015 and 2024 across nine institutions and three
					continents.
				</p>
				<p class="my-2">
					The following are examples from the training set. 'Strongly-labelled tiles' are those
					whose labels were derived through histopathology assessment. 'Weak-labelled tiles' are
					those who were not biopsied and were considered 'benign' by a doctor.
				</p>
				<img src="/assets/image/datapic.png" class="p-20" alt="" />
				<p class="font-semibold text-xl text-black my-2">Files</p>
				<ul class="list-disc ml-4">
					<li>
						<span class="text-black">train-image/</span> - image files for the training set (provided
						for train only)
					</li>
					<li>
						<span class="text-black">train-image.hdf5</span> - training image data contained in a single
						hdf5 file, with the isic_id as key
					</li>
					<li><span>train-metadata.csv</span> - metadata for the training set</li>
					<li>
						<span class="text-black">test-image.hdf5</span> - test image data contained in a single hdf5
						file, with the isic_id as key. This contains 3 test examples to ensure your inference pipeline
						works correctly. When the submitted notebook is rerun, this file is swapped with the full
						hidden test set, which contains approximately 500k images.
					</li>
					<li>
						<span class="text-black"> test-metadata.csv </span> - metadata for the test subset
					</li>
					<li>
						<span class="text-black">sample_submission.csv</span> - a sample submission file in the correct
						format
					</li>
				</ul>
				<br />
				<p class="font-semibold text-xl text-black my-2">
					Columns included only in train-metadata.csv
				</p>
				<div class="overflow-x-auto">
					<table class="border-2 table-auto w-full">
						<!-- head -->
						<thead class="border-b">
							<tr class="text-center text-lg">
								<th class="px-4 py-2">Field name</th>
								<th class="px-4 py-2">Description</th>
							</tr>
						</thead>
						<tbody>
							<!-- row 1 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">target</th>
								<td class="px-4 py-2">Binary class </td>
							</tr>
							<!-- row 2 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">lesion_id</th>
								<td class="px-4 py-2"
									>Unique lesion identifier. Present in lesions that were manually tagged as a
									lesion of interest.</td
								>
							</tr>
							<!-- row 3 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">iddx_full</th>
								<td class="px-4 py-2">Fully classified lesion diagnosis.</td>
							</tr>
							<!-- row 4 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">iddx_1</th>
								<td class="px-4 py-2">First level lesion diagnosis.</td>
							</tr>
							<!-- row 5 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">iddx_2</th>
								<td class="px-4 py-2">Second level lesion diagnosis.</td>
							</tr>
							<!-- row 6 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">iddx_3</th>
								<td class="px-4 py-2">Third level lesion diagnosis.</td>
							</tr>
							<!-- row 7 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">iddx_4</th>
								<td class="px-4 py-2">Fourth level lesion diagnosis.</td>
							</tr>
							<!-- row 8 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">iddx_5</th>
								<td class="px-4 py-2">Fifth level lesion diagnosis.</td>
							</tr>
							<!-- row 9 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">mel_mitotic_index</th>
								<td class="px-4 py-2">Mitotic index of invasive malignant melanomas.</td>
							</tr>
							<!-- row 10 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">mel_thick_mm</th>
								<td class="px-4 py-2">Thickness in depth of melanoma invasion.</td>
							</tr>
							<!-- row 11 -->
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_dnn_lesion_confidence</th>
								<td class="px-4 py-2">Lesion confidence score (0-100 scale).</td>
							</tr>
						</tbody>
					</table>
				</div>
				<p>
					'+ D’Alessandro, B. "Methods and apparatus for identifying skin features of interest." US
					Patent #11,164,670. (2021).
				</p>
				<br />
				<p class="font-semibold text-xl text-black my-2">
					Columns in both train-metadata.csv and test-metadata.csv
				</p>
				<div class="overflow-x-auto">
					<table class="border-2 table-auto w-full">
						<!-- head -->
						<thead class="border-b">
							<tr class="text-center text-lg">
								<th class="px-4 py-2">Field name</th>
								<th class="px-4 py-2">Description</th>
							</tr>
						</thead>
						<tbody>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">isic_id</th>
								<td class="px-4 py-2">Unique case identifier.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">patient_id</th>
								<td class="px-4 py-2">Unique patient identifier.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">age_approx</th>
								<td class="px-4 py-2">Approximate age of patient at time of imaging.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">sex</th>
								<td class="px-4 py-2">Sex of the person.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">anatom_site_general</th>
								<td class="px-4 py-2">Location of the lesion on the patient's body.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">clin_size_long_diam_mm</th>
								<td class="px-4 py-2">Maximum diameter of the lesion (mm).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">image_type</th>
								<td class="px-4 py-2">Structured field of the ISIC Archive for image type.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_tile_type</th>
								<td class="px-4 py-2">Lighting modality of the 3D TBP source image.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_A</th>
								<td class="px-4 py-2">A inside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_Aex</th>
								<td class="px-4 py-2">A outside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_B</th>
								<td class="px-4 py-2">B inside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_Bext</th>
								<td class="px-4 py-2">B outside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_C</th>
								<td class="px-4 py-2">Chroma inside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_Cext</th>
								<td class="px-4 py-2">Chroma outside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_H</th>
								<td class="px-4 py-2"
									>Hue inside the lesion; calculated as the angle of A* and B* in LAB* color space.</td
								>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_Hext</th>
								<td class="px-4 py-2">Hue outside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_L</th>
								<td class="px-4 py-2">L inside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_Lext</th>
								<td class="px-4 py-2">L outside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_areaMM2</th>
								<td class="px-4 py-2">Area of lesion (mm²).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_area_perim_ratio</th>
								<td class="px-4 py-2"
									>Border jaggedness, ratio between perimeter and area of lesion.</td
								>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_color_std_mean</th>
								<td class="px-4 py-2"
									>Color irregularity, calculated as the variance of colors within the lesion.</td
								>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_deltaA</th>
								<td class="px-4 py-2">Average A contrast (inside vs. outside lesion).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_deltaB</th>
								<td class="px-4 py-2">Average B contrast (inside vs. outside lesion).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_deltaL</th>
								<td class="px-4 py-2">Average L contrast (inside vs. outside lesion).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_deltaLBnorm</th>
								<td class="px-4 py-2">Contrast between the lesion and surrounding skin.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_eccentricity</th>
								<td class="px-4 py-2">Eccentricity.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_location</th>
								<td class="px-4 py-2">Classification of anatomical location.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_location_simple</th>
								<td class="px-4 py-2">Simple classification of anatomical location.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_minorAxisMM</th>
								<td class="px-4 py-2">Smallest lesion diameter (mm).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_nevi_confidence</th>
								<td class="px-4 py-2">Nevus confidence score (0-100 scale).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_norm_border</th>
								<td class="px-4 py-2">Border irregularity (0-10 scale).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_norm_color</th>
								<td class="px-4 py-2">Color variation (0-10 scale).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_perimeterMM</th>
								<td class="px-4 py-2">Perimeter of lesion (mm).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_radial_color_std_max</th>
								<td class="px-4 py-2">Color asymmetry within the lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_stdL</th>
								<td class="px-4 py-2">Standard deviation of L inside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_stdLExt</th>
								<td class="px-4 py-2">Standard deviation of L outside lesion.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_symm_2axis</th>
								<td class="px-4 py-2">Border asymmetry (0-10 scale).</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_symm_2axis_angle</th>
								<td class="px-4 py-2">Lesion border asymmetry angle.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_x</th>
								<td class="px-4 py-2">X-coordinate of the lesion on 3D TBP.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_y</th>
								<td class="px-4 py-2">Y-coordinate of the lesion on 3D TBP.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">tbp_lv_z</th>
								<td class="px-4 py-2">Z-coordinate of the lesion on 3D TBP.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">attribution</th>
								<td class="px-4 py-2">Image attribution, synonymous with image source.</td>
							</tr>
							<tr class="border-b">
								<th class="px-4 py-2 text-start">copyright_license</th>
								<td class="px-4 py-2">Copyright license.</td>
							</tr>
						</tbody>
					</table>
				</div>
				<p>
					'+ D’Alessandro, B. "Methods and apparatus for identifying skin features of interest." US
					Patent #11,164,670. (2021).
				</p>
				<br />
				<p>
					'++Betz-Stablein, B., et al. Reproducible naevus counts using 3D total body photography
					and convolutional neural networks. Dermatology. 238, 4–11 (2021).
				</p>
				<br />
				<p class="font-semibold text-xl text-black my-2">Dataset Citation</p>
				<p class="my-3">
					Please cite the SLICE-3D dataset under <span class="underline">CC BY-NC 4.0</span> with the
					following attribution:
				</p>
				<p class="bg-gray-100 text-black border p-2 rounded-lg">
					International Skin Imaging Collaboration. SLICE-3D 2024 Challenge Dataset. International
					Skin Imaging Collaboration <a
						href="https://challenge2024.isic-archive.com/"
						class="underline">https://doi.org/10.34970/2024-slice-3d</a
					> (2024). Creative Commons Attribution-Non Commercial 4.0 International License. The dataset
					was generated by the International Skin Imaging Collaboration (ISIC) and images are from the
					following sources: Hospital Clínic de Barcelona, Memorial Sloan Kettering Cancer Center, Hospital
					of Basel, FNQH Cairns, The University of Queensland, Melanoma Institute Australia, Monash University
					and Alfred Health, University of Athens Medical School, and Medical University of Vienna.
				</p>
			</div>

			<!-- รอ Back-end มาเพิ่ม -->
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
<div class="ml-64 p-6 z-0">
	<Showdata />
</div>

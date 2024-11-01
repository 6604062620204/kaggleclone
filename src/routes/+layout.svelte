<script>
	import '../app.css';
	import Navbar from './Navbar.svelte';
	let open = false;

	function handleToggle(event) {
		open = event.detail.open;
	}
</script>

<Navbar />

<slot />

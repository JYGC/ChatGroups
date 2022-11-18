<script lang="ts">
	import router from 'page';
	import userAPI from '../api/user';
	import Nav from './Nav.svelte';
	import PublicNav from './PublicNav.svelte';
	import JoinedChats from '../routes/JoinedChats.svelte';
	import MyChats from '../routes/MyChats.svelte';
	import Home from '../routes/Home.svelte';
	import Login from '../routes/Login.svelte';
	import Register from '../routes/Register.svelte';

	let page;

	router('/chats/joined', () => page = JoinedChats);
	router('/chats/my', () => page = MyChats);
	router('/home', () => page = Home);
	router('/login', () => page = Login);
	router('/register', () => page = Register);

	let loggedIn = false;
	
	router.exit(function(ctx, next) {
		loginRedirect(next);
	});

	router.start();

	userAPI.checkAuthentication((data) => {
		loggedIn = 'success' in data;
		loginRedirect(router.redirect);
	}, (error) => {
		alert(error);
	})

	$: nextPageIsPublic = publicPages.includes(page);

	// Redirect to Login if not authenticated
	const publicPages = [Login, Register];
	function loginRedirect(redirectFunction) {
		if (nextPageIsPublic && loggedIn) {
			redirectFunction('/home');
		} else if (!nextPageIsPublic && !loggedIn) {
			redirectFunction('/login');
		} else {
			redirectFunction();
		}

		//redirectFunction(); //???
	}
</script>

{#if nextPageIsPublic}
	<PublicNav />
{:else}
	<Nav />
{/if}
<svelte:component this={page} />
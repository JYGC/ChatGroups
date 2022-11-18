<script lang="ts">
    import { afterUpdate } from "svelte";


	const server = "http://0.0.0.0:8888"

	function scrollToLastItem() {
		const messagesDivs = document.querySelectorAll('.chatbox .message');
		const count = messagesDivs.length;
		if (count > 1) {
			messagesDivs[count - 1].scrollIntoView({
				behavior: 'smooth'
			});
		}
	}

	let messages = [];
	async function getMessages() {
		const response = await fetch(`${server}/message/get`);
		messages = await response.json();
	}

	var newMessage = "";
	async function sendMessage() {
		if (newMessage.trim() === '') return;
		const response = await fetch(`${server}/message/add`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({'text': newMessage})
		});
		const result = await response.json();
		if (result["success"] === true) {
			newMessage = "";
			getMessages();
		}
	}

	getMessages();

	afterUpdate(() => {
		scrollToLastItem();
	});
</script>

<main>
	<div class="chatbox">
		{#each messages as result}
			<div class="message">
				{result.text}
			</div>
		{/each}
	</div>
	<div class="form">
		<div>
			<textarea bind:value={newMessage}></textarea>
		</div>
		<div>
			<button disabled={newMessage.trim().length === 0} on:click={sendMessage}>Submit</button>
		</div>
	</div>
</main>

<style>
	main {
		text-align: left;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	.chatbox {
		height: 70vh;
		width: 100%;
		overflow: auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
<script lang="ts">
    import { getContext } from 'svelte';

    import ManageChat from './ManageChat.svelte';

    const { open } = getContext('simple-modal');

    const showSurprise = () => {
        open(ManageChat, { is_new: true });
    };
</script>
<div class="btn" on:click="{showSurprise}">Create new chat group</div>
<script lang="ts">
    export let isNew = false;

    function submit() {
        alert("ewf");
    };
</script>

<input type="text" name="name" placeholder="Chat group name" /><br />
<input type="text" name="description" placeholder="Description" /><br />
<input type="checkbox" name="visible_to_all" /><br />
<div class="btn" on:click={submit}>
    {#if isNew}
    Create new chat group
    {:else}
    Save changes
    {/if}
</div>

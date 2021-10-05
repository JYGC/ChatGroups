<script context="module" lang="ts">
    export const is_new = false;

    function submit() {
        alert("Dorn");
    }
</script>

<input type="text" name="name" placeholder="Chat group name" />
<input type="text" name="description" placeholder="Description" />
<input type="checkbox" name="visible_to_all" />
<div class="btn" on:click={submit}>
    {#if is_new}
    Create new chat group
    {:else}
    Save changes
    {/if}
</div>
<script lang="ts">
    import { Datatable, rows } from 'svelte-simple-datatables';

    import chatAPI from '../api/chat';

    export let isNew = false;

    let newChat = {
        name: null,
        description: null,
        number_of_participants: 0,
        visible_to_all: null
    }
    function submit() {
        if (
            newChat.name &&
            newChat.description &&
            newChat.number_of_participants &&
            newChat.visible_to_all !== null
        ) {
            chatAPI.createNewChat(newChat, (data) => {
                alert(data);
            }, (error) => {
                alert(error);
            });
        }
    }

    let userList;

    const settings = {
        sortable: true,
        pagination: true,
        rowPerPage: 50,
        columnFilter: true,
    };
</script>

<input type="text" name="name" placeholder="Chat group name" /><br />
<input type="text" name="description" placeholder="Description" /><br />
<input type="checkbox" name="visible_to_all" /> Anyone can join<br />
<div class="btn" on:click={submit}>
    {#if isNew}
    Create new chat group
    {:else}
    Save changes
    {/if}
</div>
{#if !isNew}
    <Datatable settings={settings} data={userList}>
        <thead>
            <th data-key="name">Name</th>
            <th data-key="description">Description</th>
            <th data-key="number_of_participants">Number of participants</th>
            <th>Options</th>
        </thead>
        <tbody>
            {#each $rows as row}
            <tr id="{row.id}">
                <td>{row.name}</td>
                <td>{row.description}</td>
                <td>{row.number_of_participants}</td>
                <td>
                    <div class="btn">Manage</div>
                </td>
            </tr>
            {/each}
        </tbody>
    </Datatable>
{/if}
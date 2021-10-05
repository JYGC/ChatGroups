<script lang="ts">
    import { Datatable, rows } from 'svelte-simple-datatables';
    import Modal from 'svelte-simple-modal';

    import chatAPI from '../api/chat';
    import ModelContent from '../components/ModelContent.svelte';

    const settings = {
        sortable: true,
        pagination: true,
        rowPerPage: 50,
        columnFilter: true,
    };

    let chatList;

    chatAPI.getAllMyChats((resp) => {
        if ('detail' in resp) {
            alert(resp['detail']);
        } else if ('success' in resp) {
            chatList = resp['success'];
        }
    }, (error) => {
        alert(error);
    });
</script>

<Modal>
    <ModelContent />
</Modal>
<Datatable settings={settings} data={chatList}>
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
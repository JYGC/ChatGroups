<!-- <script lang="ts">
    import { Datatable, rows } from 'svelte-simple-datatables';

    const settings = {
        sortable: true,
        pagination: true,
        rowPerPage: 50,
        columnFilter: true,
    };
</script>

<Datatable settings={settings}>
    <thead>
        <th>Name</th>
        <th>Number of participants</th>
        <th>Options</th>
    </thead>
    <tbody>
        {#each $rows as row}
        <tr>
            <td>{row.name}</td>
            <td>{row.description}</td>
            <td>{row.number_of_participants}</td>
            <td>
                <div class="btn">Join</div>
                {#if row.user_is_admin}
                <div class="btn">Manage</div>
                {/if}
            </td>
        </tr>
        {/each}
    </tbody>
</Datatable> -->
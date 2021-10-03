<script lang="ts">
    import userAPI from '../api/user';

    function delAll() {
        userAPI.delAll((data) => {
            alert(JSON.stringify(data));
        }, (error) => {
            alert(error);
        });
    }

    function refreshToken() {
        userAPI.refreshToken((data) => {
            alert(JSON.stringify(data));
        }, (error) => {
            alert(error);
        });
    }
</script>

<h1>Home</h1>
<div class="btn" on:click={refreshToken}>Refresh</div>
<div class="btn" on:click={delAll}>Logout</div>
<script lang="ts">
    import userAPI from '../api/user';

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

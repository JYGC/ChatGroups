<script>
    import userAPI from '../api/user';

    function logout() {
        userAPI.logout((data) => {
            alert(JSON.stringify(data));
        }, (error) => {
            alert(error);
        });
    }
</script>

<nav>
    <a href='/home'>Home</a>
    <a href='/chatgroups'>Chat groups</a>
    <a href='/' on:click={logout}>Logout</a>
</nav>
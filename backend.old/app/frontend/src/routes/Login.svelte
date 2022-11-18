<script lang="ts">
    import router from 'page';
    import userAPI from '../api/user';
    
    let warning;

    let userLogin = {
        email: null,
        password: null
    };
    function login() {
        if (userLogin.email && userLogin.password) {
            userAPI.login(userLogin, (data) => {
                if ('detail' in data) {
                    warning = data['detail'];
                } else if ('success' in data) {
                    router.redirect('/');
                }
            }, (error) => {
                warning = error;
            });
        }
    }
</script>

<h1>Login</h1>
<input type="text" name="email" bind:value={userLogin.email} placeholder="email" /><br />
<input type="password" name="password" bind:value={userLogin.password} placeholder="password" /><br />
{#if warning}
    <p style="color:red">{warning}</p><br />
{/if}
<div class="btn" on:click={login}>Login</div>

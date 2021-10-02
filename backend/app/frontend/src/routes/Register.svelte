<script>
    import userAPI from '../api/user';

    let warning;
    let userDetails = {
        email: null,
        password: null,
        phone_no: null,
        address: {
            address_no: null,
            street: null,
            suburb: null,
            state: null,
            postcode: null
        },
        dob: null
    };
    function register() {
        userAPI.register(userDetails, (data) => {
            if ('detail' in data) {
                warning = data['detail'];
            } else if ('auccess' in data) {
                router.redirect('/');
            }
        }, (error) => {
            warning = error;
        });
    }
</script>

<h1>Register</h1>
<input type="text" name="email" bind:value={userDetails.email} placeholder="email" /><br />
<input type="password" name="password" bind:value={userDetails.password} placeholder="password" /><br />
<input type="text" name="phone_no" bind:value={userDetails.phone_no} placeholder="phone number" /><br />
<input type="number" name="address_no" bind:value={userDetails.address.address_no} placeholder="street number" /><br />
<input type="text" name="street" bind:value={userDetails.address.street} placeholder="street" /><br />
<input type="text" name="suburb" bind:value={userDetails.address.suburb} placeholder="suburb" /><br />
<input type="number" name="state" bind:value={userDetails.address.state} placeholder="state" /><br />
<input type="text" name="postcode" bind:value={userDetails.address.postcode} placeholder="postcode" /><br />
<input type="date" name="dob" bind:value={userDetails.dob} placeholder="date of birth" /><br />
{#if warning}
    <p style="color:red">{warning}</p><br />
{/if}
<div class="btn" on:click={register}>Register</div>
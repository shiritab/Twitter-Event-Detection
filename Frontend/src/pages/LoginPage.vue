<template>
  <div class="container">
    <h1 class="title">Login</h1>
    <br>

    <b-form @submit.prevent="onLogin">
      <b-form-group
        id="input-group-Username"
        label-cols-sm="3"
        label="Username:"
        label-for="Username"
      >
        <b-form-input
          id="Username"
          v-model="$v.form.username.$model"
          type="text"
          :state="validateState('username')">
        </b-form-input>

        <b-form-invalid-feedback>
          Username is required
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group
        id="input-group-Password"
        label-cols-sm="3"
        label="Password:"
        label-for="Password">
        <b-form-input
          id="Password"
          type="password"
          v-model="$v.form.password.$model"
          :state="validateState('password')">
        </b-form-input>
        
        <b-form-invalid-feedback>
          Password is required
        </b-form-invalid-feedback>
      </b-form-group>

      <b-button
        type="submit"
        variant="info"
        style="width:100px;display:block;"
        class="mx-auto w-100">Login
      </b-button>
      <div class="mt-2">
        Do not have an account yet?
        <router-link to="register" style="color:red"> Register in here</router-link>
      </div>
      
    </b-form>
    <b-alert
      class="mt-2"
      v-if="form.submitError"
      variant="warning"
      dismissible
      show
    >
      Login failed: {{ form.submitError }}
    </b-alert>

  </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";
export default {
  name: "LoginPage",
  data() {
    return {
      form: {
        username: "",
        password: "",
        user_id:"",
        submitError: undefined
      },
    };
  },
  validations: {
    form: {
      username: {
        required, 
      },
      password: {
        required
      }
    }
  },
  methods: {
    validateState(param) {
      const { $dirty, $error } = this.$v.form[param];
      
      return $dirty ? !$error : null;
    },
    async Login() {
      try {
        console.log("in login section");
        console.log(this.form.username);
        const response = await this.axios.post(
          `${this.$root.serverLink}/auth/login`,
          {
            username: this.form.username,
            password: this.form.password
          }
        );
        console.log(response);
        if(response.data.user_id){
          sessionStorage.setItem('user_id', response.data.user_id);

        }
        this.$root.loggedIn = true;
        this.$root.store.user_id=response.data.user_id;
        console.log(this.$root.store.login);
        this.$root.store.login(this.form.username);
        this.$router.push("/home");
      } catch (err) {
        console.log(err.response);
        this.form.submitError = err.response.data.message;
      }



    },
    onLogin() {
      this.form.submitError = undefined;
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }

      this.Login();
    }
  }
};
</script>
<style lang="scss" scoped>
.container {
  max-width: 400px;
  margin-top: 6%;
}
.form-group{
    margin-bottom: 2rem
}
</style>
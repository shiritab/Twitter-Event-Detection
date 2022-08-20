import Vue from "vue";
import App from "./App.vue";
import VueAxios from "vue-axios";
import axios from "axios";
import routes from "./routes";
import VueRouter from "vue-router";

Vue.use(VueRouter);
const router = new VueRouter({
  routes
});

import Vuelidate from "vuelidate";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import {
    SidebarPlugin,
    NavbarPlugin,
    IconsPlugin,
    ButtonPlugin,
    FormSelectPlugin,
    CardPlugin,
    FormDatepickerPlugin,
    TablePlugin,
    LayoutPlugin,
    FormCheckboxPlugin,
    FormGroupPlugin,
    PaginationPlugin,
    FormPlugin,
    FormInputPlugin,
    FormFilePlugin,
    ToastPlugin,
    PopoverPlugin,
    
} from "bootstrap-vue";
[
    SidebarPlugin,
    NavbarPlugin,
    IconsPlugin,
    ButtonPlugin,
    FormSelectPlugin,
    CardPlugin,
    FormDatepickerPlugin,
    TablePlugin,
    LayoutPlugin ,
    FormCheckboxPlugin,
    FormGroupPlugin,
    PaginationPlugin,
    FormPlugin,
    FormInputPlugin,
    FormFilePlugin,
    ToastPlugin ,
    PopoverPlugin

].forEach((x) => Vue.use(x));
Vue.use(Vuelidate);

axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
axios.interceptors.response.use(
  function(response) {
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    return Promise.reject(error);
  }
);
axios.defaults.withCredentials = true;
Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

const shared_data = {
  username: undefined,
  login(username) {
    localStorage.setItem("username", username);
    this.username = username;
    console.log("login", this.username);
  },
  logout() {
    console.log("logout");
    localStorage.removeItem("username");
    this.username = undefined;
  }
};
console.log(shared_data);
// Vue.prototype.$root.store = shared_data;

new Vue({
  router,
  data() {
    return {
      store: shared_data,
      serverLink: "https://rps.ise.bgu.ac.il/njsw28",
    };
  },
  methods: {
    toast(title, content, variant = null, append = false) {
      this.$bvToast.toast(`${content}`, {
        title: `${title}`,
        toaster: "b-toaster-top-center",
        variant: variant,
        solid: true,
        appendToast: append,
        autoHideDelay: 3000
      });
    },
  },   
  created(){
    console.log("app created");
  },
  render: (h) => h(App)
}).$mount("#app");
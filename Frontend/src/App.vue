<template>
  <div id="app">
    <!-- <b-navbar toggleable type="dark" variant="dark">
        <b-navbar-brand :to='{ name: "home" }'>Twitter Event Detection</b-navbar-brand>
        <b-button v-b-toggle.sidebar-1>Toggle Sidebar</b-button> -->
      <b-row>
        <b-col>
          <!-- static sidebar -->
          <b-sidebar id="sidebar-border" sidebar-class="border-right border-light" bg-variant="info" text-variant="light"
           title="Twitter Event Detection" no-close-on-route-change="true" no-close-on-esc="true" no-header-close="true"
            visible="true">
            <b-navbar-nav id="nav-items" class="ml-auto">
              <!-- user context -->
              <div style="border-bottom: 2px solid rgba(219, 219, 219, 0.7);">
                <div v-if="$root.store.username">
                      <b-nav-text>{{`Welcome, ${$root.store.username}!`}}</b-nav-text>
                      <b-nav-item @click="logout()">
                        <b-icon-door-open></b-icon-door-open> Logout
                      </b-nav-item>
                </div>

                <div v-else>
                  <b-nav-text>Welcome, guest!</b-nav-text>
                  <b-nav-item :to="{ name: 'login'}">
                    <b-icon-person-circle></b-icon-person-circle> Login
                  </b-nav-item>
                </div>
              </div>

              <b-nav-item :to='{ name: "home" }'>
                <b-icon-graph-up></b-icon-graph-up> Trending
              </b-nav-item>
              <b-nav-item :to="{ name: 'compare'}">
                <b-icon-signpost-split></b-icon-signpost-split> Compare
              </b-nav-item>
              <b-nav-item :to="{ name: 'events'}">
                <b-icon-list-ul></b-icon-list-ul> Events
              </b-nav-item>
              <b-nav-item :to="{ name: 'about'}">
                <b-icon-info-circle></b-icon-info-circle> About
              </b-nav-item>
              <b-nav-item :to="{ name: 'help'}">
                <b-icon-question-circle></b-icon-question-circle> Help
              </b-nav-item>
            </b-navbar-nav>
              <!-- <template #footer="{ hide }"> -->
              <template #footer>
                <div class="d-flex bg-light text-dark align-items-center ta-center px-3 py-2">
                  <strong class="mr-auto">© Shorlak members</strong>
                  <!-- <b-button size="sm" @click="hide">Close</b-button> -->
                </div>
              </template>
          </b-sidebar>
        </b-col>
        <b-col cols="10">
          <router-view />
        </b-col>
     </b-row>

      <!-- <b-navbar-toggle v-b-toggle.sidebar-footer target="sidebar-footer">
        <template #default="{ expanded }">
            <b-icon v-if="expanded" icon="chevron-bar-up"></b-icon>
            <b-icon v-else icon="chevron-bar-down"></b-icon>
        </template>
      </b-navbar-toggle>
    </b-navbar> -->
    
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style lang="scss">
@import "./scss/form-style.scss";

#sidebar-border{
  text-align: center;
  width: 17%;
}

#nav-items a, #footer-nav-items a{
  color: white;
}

#nav-items a:hover, #footer-nav-items a:hover{
  color: black;
}


#app{
  font-family: 'Balsamiq Sans', cursive;
    /* font-family: 'Merienda', cursive; */
    text-align: center;
    background-color: whitesmoke;
    align-items: center;
  min-height: 100vh;
  // background-size: 100%;
  background-attachment: fixed;
  background-size: cover;
  // height: 100vh;
    // border: 3px;
    // box-sizing: border-box;
}

body{
margin :0px;
}

#login-sep {
  line-height: 1em;
  position: relative;
  outline: 0;
  text-align: center;
  height: 1.5em;
  opacity: 0.75;
  font-family: Arial, Helvetica, sans-serif;
}

#login-sep:before {
  background: linear-gradient(to right, transparent, rgb(172, 200, 252), transparent);
  position: absolute;
  left: 0;
  top: 50%;
  width: 100%;
  height: 2px;
}

#login-sep:after {
    position: relative;
    display: inline-block;
    padding: 0 .5em;
    line-height: 1.5em;
}
</style>
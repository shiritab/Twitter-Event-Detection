<template>
  <div id="app">
    <b-navbar toggleable type="dark" variant="dark">
        <b-navbar-brand :to='{ name: "home" }'>Twitter Event Detection</b-navbar-brand>
        <!-- <b-button v-b-toggle.sidebar-1>Toggle Sidebar</b-button> -->
        <b-sidebar id="sidebar-footer" bg-variant="dark" text-variant="light" title="Twitter Event Detection" is-nav>
            <b-navbar-nav class="ml-auto">
                <b-nav-item href="#"> # Trending</b-nav-item>
                <b-nav-item href="#"> = Compare</b-nav-item>
                <b-nav-item href="#"> + Login</b-nav-item>
                <b-nav-item :to="{ name: 'events'}"> Events </b-nav-item>
                <b-nav-item :to="{ name: 'event', params:{id:123}}"> Event </b-nav-item>
                <b-nav-item href="#" disabled>Disabled</b-nav-item>
            </b-navbar-nav>
            <template #footer="{ hide }">
              <div class="d-flex bg-light text-dark align-items-center px-3 py-2">
                <strong class="mr-auto">© Shorlak members</strong>
                <b-button size="sm" @click="hide">Close</b-button>
              </div>
            </template>
        </b-sidebar>
        <b-navbar-toggle v-b-toggle.sidebar-footer target="sidebar-footer">
            <template #default="{ expanded }">
                <b-icon v-if="expanded" icon="chevron-bar-up"></b-icon>
                <b-icon v-else icon="chevron-bar-down"></b-icon>
            </template>
        </b-navbar-toggle>
    </b-navbar>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style lang="scss">
@import "./scss/form-style.scss";

#sidebar-footer{
  text-align: center;
}
</style>
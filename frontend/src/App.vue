<template>
  <div class="font-sans" id="app">
    <TopNavbar />
    <router-view/>
  </div>
</template>

<script>
import TopNavbar from "@/components/Navbar.vue";

export default {
    name: "app",
    components: {
        TopNavbar
    }
}
</script>

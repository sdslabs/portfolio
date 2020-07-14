<template>
    <div class="font-sans" id="app">
        <TopNavbar />
        <router-view />
        <Footer v-if="!$route.meta.hideFooter" />
    </div>
</template>

<script>
import TopNavbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
    name: "app",
    components: {
        TopNavbar,
        Footer
    }
};
</script>

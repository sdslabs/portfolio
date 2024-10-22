<template>
    <div class="font-sans" id="app">
        <MarqueeSlider />
        <TopNavbar />
        <router-view />
        <Footer v-if="!$route.meta.hideFooter" />
    </div>
</template>

<script>
import TopNavbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";
// import MarqueeSlider from "@/components/Slider.vue";

export default {
    name: "app",
    components: {
        // MarqueeSlider  ,
        TopNavbar,
        Footer
    }
};
</script>

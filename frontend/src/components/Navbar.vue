<template>
    <nav :class="scrolled ? 'shadow-sm': ''" class="fixed font-sans antialiased bg-white flex justify-between items-center flex-wrap py-4 px-16 sm:py-8 sm:px-36 w-full z-10">
        <div class="flex items-center flex-no-shrink">
            <router-link to="/" class="block">
                <img alt="SDSLabs Logo" class="w-48 h-12" src="@/assets/images/logo.png">
            </router-link>
        </div>
        <div class="block sm:hidden">
            <button @click="toggle" class="flex items-center px-6 py-4 border rounded">
                <svg class="fill-current h-6 w-6" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
            </button>
        </div>
        <div :class="open ? 'block': 'hidden'" class="relative w-full flex-grow sm:flex sm:items-center sm:w-auto z-10">
            <div class="text-sm text-black leading-normal sm:flex justify-center sm:flex-grow ">
                <NavLink v-bind:native=false v-bind:last=false url="/projects" text="PROJECTS" />
                <NavLink v-bind:native=false v-bind:last=false url="/news" text="NEWS" />
                <NavLink v-bind:native=true v-bind:last=false url="https://blog.sdslabs.co/" text="BLOG" />
                <NavLink v-bind:native=false v-bind:last=false url="/about" text="ABOUT US" />
                <NavLink v-bind:native=false v-bind:last=true url="/contact" text="CONTACT" />
            </div>
        </div>
        <div :class="open ? 'block': 'hidden'" class="text-sm sm:flex mt-4 sm:mt-0">
            <Button v-bind:native=true url="https://accounts.sdslabs.co/" text="LOGIN" />
        </div>
    </nav>
</template>

<script>

import NavLink from "@/components/navbar/NavLink.vue";
import Button from "@/components/Button.vue";

export default {
    name: "TopNavbar",
    data: function initData() {
        return {
            open: false,
            scrolled: false
        };
    },
    methods: {
        toggle: function toggle() {
            this.open = !this.open;
        },
        handleScroll: function handleScroll() {
            this.scrolled = window.scrollY > 0;
        }
    },
    created () {
        window.addEventListener('scroll', this.handleScroll);
    },
    destroyed() {
        window.removeEventListener('scroll', this.handleScroll);
    },
    components: {
        NavLink,
        Button
    }
};
</script>

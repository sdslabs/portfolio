<template>
    <div class="font-sans antialiased" id="nav">
        <nav class="flex justify-between flex-wrap py-2 px-8 sm:py-8 sm:px-36">
            <div class="flex items-center flex-no-shrink mr-6">
                <router-link to="/" class="block">
                    <img alt="SDSLabs Logo" class="w-48 h-12" src="..//assets/images/logo.png">
                </router-link>
            </div>
            <div class="block sm:hidden">
                <button @click="toggle" class="flex items-center px-3 py-2 border rounded">
                    <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
                </button>
            </div>
            <div :class="open ? 'block': 'hidden'" class="w-full flex-grow sm:flex sm:items-center sm:w-auto">
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
    </div>
</template>

<script>

import NavLink from "@/components/navbar/NavLink.vue";
import Button from "@/components/Button.vue";

export default {
    name: "TopNavbar",
    data: function initData() {
        return {
            open: false
        };
    },
    methods: {
        toggle: function toggle() {
            this.open = !this.open;
        }
    },
    components: {
        NavLink,
        Button
    }
};
</script>

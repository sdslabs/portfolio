<template>
    <nav
        :class="scrolled ? 'shadow-sm' : ''"
        class="fixed font-sans antialiased bg-white flex justify-between items-center flex-wrap py-12 px-16 sm:py-8 sm:px-36 w-full z-30"
    >
        <div class="flex items-center flex-no-shrink">
            <router-link to="/" class="block">
                <img
                    alt="SDSLabs Logo"
                    class="h-14 -ml-6 sm-ml-0 sm:w-48 sm:h-12"
                    src="@/assets/images/logo.svg"
                />
            </router-link>
        </div>
        <div class="block sm:hidden">
            <button
                @click="toggle"
                class="flex items-center px-6 py-4 border rounded"
            >
                <img class="hamburger" src="@/assets/images/hamburger.svg" />
            </button>
        </div>

        <div
            :class="open ? 'block' : 'hidden'"
            class="relative w-full flex-grow sm:flex sm:items-center sm:w-auto z-10 hidden"
        >
            <div
                class="text-sm text-black leading-normal sm:flex justify-center sm:flex-grow "
            >
                <NavLink
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/projects"
                    text="PROJECTS"
                />
                <NavLink
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/news"
                    text="NEWS"
                />
                <NavLink
                    v-bind:native="true"
                    v-bind:last="false"
                    url="https://blog.sdslabs.co/"
                    text="BLOG"
                />
                <NavLink
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/about"
                    text="ABOUT US"
                />
                <NavLink
                    v-bind:native="true"
                    v-bind:last="true"
                    url="http://chat.sdslabs.co/"
                    text="CONTACT"
                />
            </div>
        </div>
        <div
            :class="open ? 'block' : 'hidden'"
            class="text-sm sm:flex mt-4 sm:mt-0 hidden"
        >
            <Button
                v-bind:native="true"
                url="https://accounts.sdslabs.co/"
                text="Login"
            />
        </div>
        <div :class="open ? 'block' : 'hidden'" class="fixed -ml-16 -mt-21">
            <NavMobile :open="open" @click="toggle" />
        </div>
    </nav>
</template>

<script>
import NavLink from "@/components/navbar/NavLink.vue";
import NavMobile from "@/components/navbar/NavMobile.vue";
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
    created() {
        window.addEventListener("scroll", this.handleScroll);
    },
    destroyed() {
        window.removeEventListener("scroll", this.handleScroll);
    },
    components: {
        NavLink,
        Button,
        NavMobile
    }
};
</script>

<style lang="scss" scoped>
.hamburger::selection {
    background-color: transparent;
}
.hamburger::-moz-selection {
    background-color: transparent;
}
.hamburger {
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
</style>

<template>
    <div
        v-bind:class="{
            'bg-grey': open,
            'bg-transparent': !open,
            navhide: !open && !active
        }"
        class="fixed h-full w-full z-30 sm:hidden"
        @click="close"
    >
        <nav
            v-bind:class="{
                nav: open,
                navclose: !open && active,
                navhide: !open && !active
            }"
            class="fixed h-full bg-white w-3/4 ml-1/4 flex flex-col"
        >
            <div class="self-end mt-16 mr-22 h-8 w-8">
                <img src="@/assets/images/close.svg" />
            </div>
            <div
                class="text-lg text-black leading-normal justify-center mt-20 pl-12"
            >
                <NavLink
                    class="py-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/projects"
                    text="PROJECTS"
                    @click="close"
                />
                <NavLink
                    class="py-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/news"
                    text="NEWS"
                    @click="close"
                />
                <NavLink
                    class="py-6"
                    v-bind:native="true"
                    v-bind:last="false"
                    url="https://blog.sdslabs.co/"
                    text="BLOG"
                    @click="close"
                />
                <NavLink
                    class="py-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/about"
                    text="ABOUT US"
                    @click="close"
                />
                <NavLink
                    class="py-6"
                    v-bind:native="true"
                    v-bind:last="true"
                    url="http://chat.sdslabs.co"
                    text="CONTACT"
                    @click="close"
                />
            </div>
            <div class="text-sm mt-14 ml-12 mr-12">
                <Button
                    class="w-full h-24 pb-20 text-center text-2xl"
                    v-bind:native="true"
                    url="https://accounts.sdslabs.co/"
                    text="Login"
                    @click="close"
                />
            </div>
        </nav>
    </div>
</template>

<script>
import NavLink from "@/components/navbar/NavLink.vue";
import Button from "@/components/Button.vue";
export default {
    name: "NavMobile",
    components: {
        NavLink,
        Button
    },
    props: {
        open: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            active: false
        };
    },
    methods: {
        close() {
            this.active = true;
            this.$emit("click");
            setTimeout(() => {
                let vm = this;
                vm.active = false;
            }, 500);
        }
    }
};
</script>

<style lang="scss" scoped>
@keyframes slideIn {
    0% {
        transform: translate(100%, 0%);
        opacity: 1;
    }
    100% {
        transform: translate(0%, 0%);
        opacity: 1;
    }
}
@keyframes slideOut {
    0% {
        transform: translate(0%, 0%);
        opacity: 1;
    }
    100% {
        transform: translate(100%, 0%);
        opacity: 1;
        display: none;
    }
}
.nav {
    animation: slideIn 0.5s ease forwards;
}
.navclose {
    animation: slideOut 0.5s ease forwards;
}
.navhide {
    display: none;
}
</style>

<template>
    <div class="fixed h-full w-full bg-grey z-30">
        <nav

            class="fixed h-full bg-white w-3/4 ml-1/4 flex flex-col">
            <div class="self-end mt-20 mr-16 h-8 w-8"><img src="@/assets/images/close.svg"/></div>
            <div
                class="text-lg text-black leading-normal justify-center mt-20 pl-12"
            >
                <NavLink
                    class="pt-6 pb-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/projects"
                    text="PROJECTS"
                />
                <NavLink
                    class="pt-6 pb-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/feed"
                    text="FEED"
                />
                <NavLink
                    class="pt-6 pb-6"
                    v-bind:native="true"
                    v-bind:last="false"
                    url="https://blog.sdslabs.co/"
                    text="BLOG"
                />
                <NavLink
                    class="pt-6 pb-6"
                    v-bind:native="false"
                    v-bind:last="false"
                    url="/about"
                    text="ABOUT US"
                />
                <NavLink
                    class="pt-6 pb-6"
                    v-bind:native="false"
                    v-bind:last="true"
                    url="/contact"
                    text="CONTACT"
                />
            </div>
            <div
                class="text-sm mt-14 ml-12 mr-12"
            >
                <Button
                    class="w-full h-24 text-center text-2xl leading-tight"
                    v-bind:native="true"
                    url="https://accounts.sdslabs.co/"
                    text="Login"
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
    }
}
</script>

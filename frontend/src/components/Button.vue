<template>
    <a
        v-if="native"
        :href="url"
        class="no-underline bg-black inline-block font-bold text-base text-white leading-none px-14 py-5 border-solid border-black border-1"
        target="blank"
    >
        {{ text }}
    </a>
    <router-link
        v-else
        :href="url"
        class="no-underline bg-black inline-block font-bold text-base text-white leading-none px-14 py-5 border-solid border-black border-1"
    >
        {{ text }}
    </router-link>
</template>

<script>
export default {
    name: "Button",
    props: {
        native: Boolean,
        url: String,
        text: String
    }
};
</script>

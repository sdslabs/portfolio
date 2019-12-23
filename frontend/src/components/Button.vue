<template>
    <a
        v-if="native"
        :href="url"
        class="no-underline inline-block text-sm text-black leading-none px-14 py-5 border-solid border-black border-1 rounded"
        target="blank"
    >
        {{ text }}
    </a>
    <router-link
        v-else
        :href="url"
        class="no-underline inline-block text-sm text-black leading-none px-14 py-5 border-solid border-black border-1 rounded"
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

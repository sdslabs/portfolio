<template>
    <div
        class="w-auto inline-block h-16 sm:h-12 bg-label text-xl sm:text-sm font-extrabold leading-normal pl-5 pr-6 pt-3 pb-3 text-center"
    >
        {{ text.toUpperCase() }}
    </div>
</template>

<script>
export default {
    name: "label",
    props: {
        text: String
    }
};
</script>

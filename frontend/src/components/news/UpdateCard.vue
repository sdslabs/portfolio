<template>
    <div>
        <div class="mt-12 font-extrabold text-base leading-180">{{title}}</div>
        <div class="mt-5 text-base leading-normal">{{description}}</div>
    </div>
</template>

<script>
export default {
    name: "updateCard",
    props: {
        title: String,
        description: String
    }
}
</script>

<template>
    <div class="flex flex-col pt-60 w-full">
        <div
            class="flex md:flex-row-reverse items-center justify-between md:justify-between flex-col pl-0 pr-0"
        >
            <div
                class="flex flex-row items-center justify-center md:ml-64 md:mr-60"
            >
                <img class="img1 w-72" src="@/assets/images/labs1.svg" />
                <img
                    class="img2 w-88 md:pt-96 md:pl-0"
                    src="@/assets/images/labs2.svg"
                />
                <img
                    class="img3 w-88 md:mb-64 md:-ml-52"
                    src="@/assets/images/labs3.svg"
                />
            </div>
            <div class="flex flex-col md:pl-60 pr-0 pt-24 md:pt-0">
                <div class="text-3xl font-extrabold">What is SDSLabs</div>
                <div class="w-140 md:w-180 pt-10 text-lg text-grey leading-170">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada
                    nisl. Pellentesque sagittis fringilla tempor. Pellentesque
                    sit amet augue sit amet quam feugiat porta vitae sit amet
                    ligula. Nulla posuere pellentesque metus sit amet.
                </div>
            </div>
        </div>
        <div
            class="flex md:flex-row items-center md:justify-between md:ml-64 md:mr-64 pt-36 flex-col pl-0 pr-0"
        >
            <Gallery class="" />
            <div class="flex flex-col md:pr-14 md:pt-0 pr-0 pt-72">
                <div class="text-3xl font-extrabold">What we do</div>
                <div class="w-140 pt-10 text-lg text-grey leading-170">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada
                    nisl. Pellentesque sagittis fringilla tempor. Pellentesque
                    sit amet augue sit amet quam feugiat porta vitae sit amet
                    ligula.
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Gallery from "@/components/Gallery.vue";
export default {
    name: "about",
    components: {
        Gallery
    }
};
</script>

<style lang="scss" scoped>
@media screen and (max-width: 576px) {
    .img1 {
        width: 9.625rem;
        height: 9.0625rem;
    }

    .img2 {
        width: 11.25rem;
        height: 10.3125rem;
    }

    .img3 {
        width: 12.125rem;
        height: 12.125rem;
    }
}
</style>

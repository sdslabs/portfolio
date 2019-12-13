<template>
    <div class="flex flex-col md:pt-44 pt-48 w-full">
        <div
            class="flex flex-col-reverse md:flex-row-reverse items-center justify-between md:justify-between flex-col pl-0 pr-0"
        >
            <div
                class="flex flex-row justify-center mt-12 ml-6 mr-6 md:ml-64 md:mr-60"
            >
                <img class="img1 w-72" src="@/assets/images/labs1.svg" />
                <img
                    class="img2 w-88 pt-52 md:pt-96 md:pl-0"
                    src="@/assets/images/labs2.svg"
                />
                <img
                    class="img3 w-88 md:mb-64 md:-ml-52"
                    src="@/assets/images/labs3.svg"
                />
            </div>
            <div class="flex flex-col ml-6 mr-6 md:w-auto md:pl-60 pr-0 md:pt-24 md:pt-0">
                <div class="text-3xl font-extrabold">What is SDSLabs</div>
                <div class="md:w-180 pt-10 text-lg text-grey leading-170">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada
                    nisl. Pellentesque sagittis fringilla tempor. Pellentesque
                    sit amet augue sit amet quam feugiat porta vitae sit amet
                    ligula. Nulla posuere pellentesque metus sit amet.
                </div>
            </div>
        </div>
        <div
            class="flex flex-col-reverse mt-28 md:flex-row md:justify-between md:ml-64 md:mr-64 md:pt-36"
        >
            <div class="mt-16 md:mt-0 ml-6 mr-6"><Gallery/></div>
            <div class="flex flex-col mr-6 ml-6 md:w-auto md:pr-14 md:pt-8">
                <div class="text-3xl font-extrabold">What we do</div>
                <div class="md:w-140 pt-10 text-lg text-grey leading-170">
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
        width: 12.78rem;
        height: 10.326rem;
        margin-top: 3.3rem;
    }

    .img2 {
        width: 13.18rem;
        height: 8.92rem;
        margin-top: 11.5rem;
        margin-left: 0.7rem;
    }

    .img3 {
        width: 14.213rem;
        height: 8.99rem;
    }
}
</style>

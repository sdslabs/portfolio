<template>
    <div class="flex flex-col pt-60 w-full pb-20">
        <div
            class="flex md:flex-row-reverse items-center justify-between md:justify-between flex-col pl-0 pr-0"
        >
            <div
                class="flex flex-row items-center justify-center md:ml-44 md:mr-56"
            >
                <img class="img1 w-72" src="@/assets/images/labs1.svg" />
                <img
                    class="img2 w-88 md:pt-56 md:pl-8"
                    src="@/assets/images/labs2.svg"
                />
                <img
                    class="img3 w-88 md:pb-32"
                    src="@/assets/images/labs3.svg"
                />
            </div>
            <div class="flex flex-col md:pl-56 pr-0 pt-24 md:pt-0">
                <div class="text-3xl font-extrabold">What is SDSLabs</div>
                <div class="w-100 md:w-108 pt-10 text-lg text-grey leading-170">
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
            <div class="flex flex-col md:pr-14 md:pt-0 pr-0 pt-64">
                <div class="text-3xl font-extrabold">What we do</div>
                <div class="w-100 pt-10 text-lg text-grey leading-170">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada
                    nisl. Pellentesque sagittis fringilla tempor. Pellentesque
                    sit amet augue sit amet quam feugiat porta vitae sit amet
                    ligula.
                </div>
            </div>
        </div>
        <div class="area_of_interest">
            <div
                class="flex md:flex-row-reverse items-center md:justify-between flex-col"
            >
                <div class="mr-28 w-220 relative">
                    <div class="flex rounded shadow-md absolute flex-row w-92 h-32">
                        <div class="m-8 w-20 h-20"><img src="@/assets/images/interest1.png"></div>
                        <div class="mt-6 font-sans font-semibold text-base align-middle leading-160">Software Development</div>
                    </div>
                    <div class="md:pt-0 md:pl-100">
                        <div class="flex absolute rounded shadow-md mt-20 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20"><img src="@/assets/images/interest2.png"></div>
                            <div class="mt-6 font-sans font-semibold text-base align-middle leading-160">Information Security</div>
                        </div>
                    </div>
                    <div class="md:pt-22">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20"><img src="@/assets/images/interest3.png"></div>
                            <div class="mt-12 font-sans font-semibold text-base align-middle leading-160">Product Design</div>
                        </div>
                    </div>
                    <div class="md:pt-20 md:pl-100">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20"><img src="@/assets/images/interest4.png"></div>
                            <div class="mt-12 font-sans font-semibold text-base leading-160">Data Science</div>
                        </div>
                    </div>
                    <div class="md:pt-22">
                        <div class="flex absolute rounded shadow-md mt-20 mr-0 flex-row w-92 h-32">
                            <div class="m-8 w-20 h-20"><img src="@/assets/images/interest5.png"></div>
                            <div class="mt-6 font-sans font-semibold text-base align-middle leading-160">Game Development</div>
                        </div>
                    </div>

                </div>

                <div class="flex flex-col md:pl-56 relative w-180 h-76">
                    <div class="text-3xl font-black absolute mt-12">Area of Interest</div>
                    <div class="text-base w-180 mt-40 absolute font-semibold text-grey leading-170">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                        Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada
                        nisl. Pellentesque sagittis fringilla tempor. Pellentesque
                        sit amet augue sit amet quam feugiat porta vitae sit amet
                        ligula. Nulla posuere pellentesque metus sit amet.
                    </div>
                </div>
            </div>
        </div>

        <div class="timeline">
            <div
                class="flex md:flex-col items-center w-screen md:justify-between flex-col mt-176 relative"
            >
                <div class="text-3xl font-black absolute">Timeline</div>
                <div class="text-base w-292 mt-28 text-center absolute font-semibold text-grey leading-170">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor. Pellentesque sit amet augue sit amet quam feugiat porta vitae sit amet ligula.</div>
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

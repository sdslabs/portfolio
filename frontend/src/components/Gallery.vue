<template>
    <div class="gallery w-gallery">
        <img
            class="h-88 md:h-128 md:w-108"
            src="@/assets/images/image 3.3.png"
            alt="image"
        />
        <div
            class="textbox absolute w-96 h-64 ml-44 -mt-32 md:w-98 md:h-88 md:ml-98 md:mt-gallery bg-white z-30"
        >
            <div class="font-extrabold md:text-lg mt-10 ml-10">Lectures</div>
            <div
                class="w-88 md:w-96 leading-170 text-grey md:text-base mt-8 ml-10"
            >
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean
                ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl.
                Pellentesque sagittis fringilla tempor. Lorem ipsum dolor
            </div>
        </div>
        <div>
            <span></span>
        </div>
    </div>
</template>

<script>
export default {
    name: "Gallery"
};
</script>

<style scoped lang="scss">
.textbox {
    box-shadow: 0px 6px 30px rgba(0, 0, 0, 0.07);
    border-radius: 5px;
}
</style>

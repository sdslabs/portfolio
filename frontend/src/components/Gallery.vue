<template>
    <div class="gallery w-gallery">
        <div><img class="h-72 w-96" src="@/assets/images/image 3.3.png" alt="image"></div>
        <div class="textbox absolute w-88 h-56 ml-64 mt-gallery bg-white z-30">
            <div class="font-extrabold mt-6 ml-6">Lectures</div>
            <div class="w-72 leading-170 text-grey mt-5 ml-6">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac lacinia nisi, ac maximus sem. Ut eu malesuada nisl. Pellentesque sagittis fringilla tempor. Lorem ipsum dolor</div>
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

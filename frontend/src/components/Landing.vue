<template>
    <div>
        <div
            class="banner pt-56 sm:pt-navbar px-16 relative flex flex-col justify-center items-center sm:px-0 sm:justify-between sm:flex-row"
        >
            <div class="hidden sm:flex w-88 h-full items-center justify-center">
                <img class="w-full pb-20" src="@/assets/images/home1.svg" />
            </div>
            <div
                class="sm:h-full sm:flex sm:flex-1 flex-col items-center justify-center"
            >
                <h1
                    class="text-4.5xl sm:text-5xl text-center font-extrabold leading-170"
                >
                    THINK. BUILD. SHIP.
                </h1>
                <p
                    class="text-1.5xl sm:text-xl font-semibold text-center pt-14 sm:w-5/7 leading-160 opacity-60"
                >
                    We at SDSLabs are a bunch of designers and developers who
                    aim to encourage the development of technology and
                    innovation in IITR campus (and beyond) by learning, sharing
                    knowledge and solving problems.
                </p>
            </div>
            <div
                class="w-screen sm:w-88 flex flex-row-reverse justify-between sm:h-full sm:items-center sm:justify-center"
            >
                <div>
                    <img
                        class="w-60 sm:w-88 pt-8 sm:pt-20"
                        src="@/assets/images/home2.svg"
                    />
                </div>
                <div>
                    <img
                        class="w-60 sm:hidden sm:w-full pt-8"
                        src="@/assets/images/home1.svg"
                    />
                </div>
            </div>
        </div>
        <div class="banner-footer flex justify-center items-start">
            <router-link
                to="/projects"
                class="inline-flex flex-col items-center no-underline text-base"
            >
                <img
                    class="pt-16 sm:pt-0 block sm:h-10"
                    src="@/assets/images/down-arrow.svg"
                />
                <span class="block text-grey pt-4 font-semibold text-lg"
                    >Projects</span
                >
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "landing"
};
</script>

<style scoped lang="scss">
.banner {
    height: 80vh;
}

.banner-footer {
    height: 20vh;
}

.text-justify {
    text-align-last: center;
}
</style>

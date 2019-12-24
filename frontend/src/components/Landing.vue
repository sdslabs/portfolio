<template>
    <div>
        <div
            class="banner pt-navbar px-16 relative flex flex-col justify-center items-center sm:px-0 sm:justify-between sm:flex-row"
        >
            <div class="hidden sm:flex w-88 h-full items-center justify-center">
                <img class="w-full pb-20" src="@/assets/images/home1.svg" />
            </div>
            <div
                class="sm:h-full sm:flex sm:flex-1 flex-col items-center justify-center"
            >
                <h1 class="text-5xl text-justify font-extrabold leading-170">
                    THINK. BUILD. SHIP.
                </h1>
                <p
                    class="text-xl text-justify pt-14 sm:w-4/7 leading-160 opacity-60"
                >
                    Commodo aute aliquip excepteur incididunt ut magna minim
                    esse sit elit. Aute mollit veniam laborum reprehenderit
                    tempor est aute enim. Proident deserunt laborum
                    reprehenderit ut.
                </p>
            </div>
            <div
                class="w-screen md:w-88 flex flex-row-reverse justify-between sm:h-full sm:items-center sm:justify-center"
            >
                <div>
                    <img
                        class="w-60 md:w-88 pt-20"
                        src="@/assets/images/home2.svg"
                    />
                </div>
                <div>
                    <img
                        class="w-60 sm:hidden sm:w-full pt-20"
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
                    class="pt-16 sm:pt-0 block"
                    src="@/assets/images/down-arrow.svg"
                />
                <span class="block text-black pt-4">Projects</span>
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

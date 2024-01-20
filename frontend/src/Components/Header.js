import React from "react";

const Header = () => {
  return (
    <section class="bg-white text-gray-900">
      <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
        <div class="mx-auto max-w-3xl text-center">
          <h1 class="bg-gradient-to-r from-teal-300 via-teal-500 to-teal-700 bg-clip-text text-3xl font-extrabold text-transparent sm:text-5xl">
            Understand User Flow.
            <span class="sm:block"> Increase Conversion. </span>
          </h1>

          <p class="mx-auto mt-4 max-w-xl sm:text-xl/relaxed">
            Unlock a world of possibilities for your file formats! Discover a
            comprehensive suite of 100% FREE tools to convert "csv", "json",
            "parquet", "excel" your files effortlessly.
          </p>

          <div class="mt-8 flex flex-wrap justify-center gap-4">
            <a
              class="block w-full rounded border border-teal-600 bg-teal-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-black focus:outline-none focus:ring active:text-opacity-75 sm:w-auto"
              href="/get-started"
            >
              Get Started
            </a>

            <a
              class="block w-full rounded border border-teal-600 px-12 py-3 text-sm font-medium text-black hover:bg-teal-600 hover:text-white focus:outline-none focus:ring active:bg-teal-500 sm:w-auto"
              href="/about"
            >
              Learn More
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Header;

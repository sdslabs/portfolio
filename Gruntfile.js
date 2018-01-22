module.exports = function(grunt){
  grunt.initConfig({
    pkg : grunt.file.readJSON('package.json'),

    stc: {
      src: 'src',
      dist: 'dist'
    },

    copy: {
      dev: {
        files: [{
          expand: true,
          dot: true,
          cwd: '<%= stc.src %>',
          dest: '<%= stc.dist %>',
          src: [
            '**/*.{js,html,ico,png,jpg,jpeg,gif,txt,svg,pdf,css,ttf,otf}',
            '.htaccess'
          ]
        }]
      },

      images : {
        files: [{
          expand: true,
          dot: true,
          cwd: '<%= stc.src %>/images',
          dest: '<%= stc.dist %>/images',
          src: ['**/*.{ico,png,jpg,jpeg,gif,svg}']  
        }]
      },
      html : {
        files: [{
          expand: true,
          dot: true,
          cwd: '<%= stc.src %>',
          dest: '<%= stc.dist %>',
          src: ['**/*.html', '.htaccess']
        }]
      },
      js : {
        files: [{
          expand: true,
          dot: true,
          cwd: '<%= stc.src %>/scripts',
          dest: '<%= stc.dist %>/scripts',
          src: ['**/*.js']
        }]
      },
      prod: {
        files: [{
          expand: true,
          dot: true,
          cwd: '<%= stc.src %>',
          dest: '<%= stc.dist %>',
          src: [
            '**/*.{ico,png,svg,txt,pdf,css}',
            '.htaccess',
          ]
        }]  
      },
      server: {
        files: [{
          expand: true,
          cwd: '<%= stc.src %>/server',
          dest: '<%= stc.dist %>/server',
          src: '**/*'
        }]
      }
    },

    clean: {
      dist: {
        files: [{
          dot: true,
          src: [
            '<%= stc.dist %>',
            '!<%= stc.dist %>/.git*'
          ]
        }]
      },
      images: {
        files: [{
          dot: true,
          src: ['<%= stc.dist %>/images/**/*.{ico,png,jpg,jpeg,gif,svg}']
        }]
      },
      html: {
        files: [{
          dot: true,
          src: ['<%= stc.dist %>/**/*.html']
        }]
      },
      js: {
        files: [{
          dot: true,
          src: ['<%= stc.dist %>/scripts/**/*.js']
        }]
      }
    },

    htmlmin: {
      dist: {
        options: {
          collapseBooleanAttributes: true,
          collapseWhitespace: true,
          removeAttributeQuotes: true,
          removeCommentsFromCDATA: true,
          removeEmptyAttributes: true,
          useShortDoctype: true
        },
        files: [{
          expand: true,
          cwd: '<%= stc.src %>',
          src: '**/*.html',
          dest: '<%= stc.dist %>'
        }]
      }
    },

    imagemin: {
      dist: {
        options: {
          optimizationLevel: 5
        },
        files: [{
          expand: true,
          cwd: '<%= stc.src %>/images',
          src: ['**/*.{png,jpg,gif}'],
          dest: '<%= stc.dist %>/images'
        }]
      }
    },

    uglify: {
      dist: {
        options: {
          banner: '/*! script.js 1.0.0 | Ankit Kataria */'
        },
        files : [{
          expand: true,
          cwd: '<%= stc.src %>/scripts',
          src: ['**/*.js', '!*.min.js'],
          dest: '<%= stc.dist %>/scripts'
        }]
        }
    },

    sass: {
      dist: {
        files : [{
          expand: true,
          cwd: 'src/styles',
          src: ['**/*.scss'],
          dest: 'dist/styles',
          ext: '.css'
        }]
      }
    },

    cssmin: {
      dist: {
        options: {
          banner: '/*! style.css 1.0.0 | Ankit Kataria */'
        },
        files: [{
          expand: true,
          cwd: '<%= stc.dist %>/styles',
          src: ['**/*.css', '!*.min.css'],
          dest: '<%= stc.dist %>/styles'
        }]
      }
    },

    connect: {
      options: {
          port: 5000,
          livereload: 35729,
          hostname: '0.0.0.0',
      },

      livereload: {
          options: {
              open: true,
              base: ['<%= stc.dist %>'],
              middleware: function (connect, options) {
                  if (!Array.isArray(options.base)) {
                      options.base = [options.base];
                  }
                  var serveStatic = require('serve-static');
                  var middlewares = [require('connect-livereload')()];
                  options.base.forEach(function(base) {
                      middlewares.push(serveStatic(base));
                  });
                  return middlewares;
              }
          }
      }
    },    

    watch: {
      scss: {
        files: 'src/styles/**/*.scss',
        tasks : ['sass'],
        options: {
              livereload: '<%= connect.options.livereload %>',
          }
      },
      images: {
        files: 'src/images/**/*.{png,jpeg,jpg,ico,svg}',
        tasks : ['clean:images','copy:images'],
        options: {
              livereload: '<%= connect.options.livereload %>',
          }
      },
      html: {
        files: 'src/**/*.html',
        tasks: ['clean:html','copy:html'],
        options: {
              livereload: '<%= connect.options.livereload %>',
          }
      },
      js: {
        files: 'src/scripts/**/*.js',
        tasks: ['clean:js','copy:js'],
        options: {
              livereload: '<%= connect.options.livereload %>',
          }
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-htmlmin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.registerTask('default',[ "clean:dist", "sass", "copy:dev", "connect:livereload", "watch" ]);
  grunt.registerTask('build', [ "clean:dist", "sass", "cssmin", "uglify", "imagemin", "htmlmin", "copy:prod", "copy:server" ]);
}
module.exports = function(grunt) {
    'use strict';

    var isDev = (grunt.option('dev') !== undefined) ? Boolean(grunt.option('dev')) : process.env.GRUNT_ISDEV === '1';
    var pkg = grunt.file.readJSON('package.json');

    if (isDev) {
        grunt.log.subhead('Running Grunt in DEV mode');
    }

    grunt.initConfig({
        pkg: pkg,

        sass: {
            compile: {
                files: {
                    'static/css/main.min.css': 'static/scss/main.scss'
                },
                options: {
                    style: 'compressed',
                    sourcemap: isDev ? 'auto' : 'none'
                }
            }
        },

        watch: {
            css: {
                files: ['static/scss/*.scss'],
                tasks: ['sass']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['sass']);
};

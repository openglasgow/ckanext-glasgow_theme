module.exports = function(grunt) {


	// register all that available tasks
	require("matchdep").filterDev("grunt-*").forEach(grunt.loadNpmTasks);

	// initial optipns
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        watch: {
            options: {
                //livereload: true,
            },
            css: {
                files: ['less/**/*.less'],  
                tasks: ['buildcss']
            }
        },

        less: {
          development: {
            options: {
              paths: ["less"],
              sourceMap: false,
              sourceMapFilename: "source.map"
            },
            files: {
              "glasgow_main.css": "less/glasgow_main.less"
            }
          }
        }
		
    }) // end grunt.initCofig


    grunt.registerTask('buildcss', ['less']);


}
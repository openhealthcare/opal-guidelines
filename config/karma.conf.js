module.exports = function(config){
  var opalPath;
  if(process.env.TRAVIS){
    python_version = process.env.TRAVIS_PYTHON_VERSION;
    opalPath = '/home/travis/virtualenv/python' + python_version + '/src/opal';
  }
  else{
    opalPath = '../../opal';
  }
  var karmaDefaults = require(opalPath + '/config/karma_defaults.js');
  var baseDir = '../' + __dirname;
  var coverageFiles = [
    __dirname +  '/../guidelines/static/js/guidelines/controllers/*.js'
  ];
  var includedFiles = [
    __dirname +  '/../guidelines/static/js/guidelines/controllers/*.js',
    __dirname + '/../guidelines/static/js/test/*.js',
  ];

  var defaultConfig = karmaDefaults(coverageFiles, includedFiles, baseDir);
  config.set(defaultConfig);
};

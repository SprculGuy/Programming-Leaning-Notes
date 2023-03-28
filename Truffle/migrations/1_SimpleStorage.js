var simplestorage = artifacts.require("./SimpleStorage.sol");

module.exports = function(deployer){
    deployer.deploy(simplestorage);
};

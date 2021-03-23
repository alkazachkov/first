Vagrant.configure("2") do |config|
  config.vm.define "node-1" do |node1|
    node1.vm.box = "ubuntu/bionic64"
    node1.vm.network "forwarded_port", guest: 80, host: 8081
    node1.vm.network "private_network" , ip: "192.168.10.23", :adapter => 2

  end

  config.vm.define "node-2" do |node2|
    node2.vm.box = "ubuntu/bionic64"
    node2.vm.network "forwarded_port", guest: 80, host: 8080
    node2.vm.network "forwarded_port", guest: 443, host: 8443
    node2.vm.network "forwarded_port", guest: 8822, host: 8022
    node2.vm.network "private_network" , ip: "192.168.10.24", :adapter => 2

      config.vm.provider "virtualbox" do |v|
        v.memory = 4048
        v.cpus = 4
      end
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end

Vagrant.configure("2") do |config|
  #config.vm.box = "ubuntu/bionic64"
  config.vm.define "node-1" do |node1|
    node1.vm.box = "ubuntu/bionic64"
  end

  config.vm.define "node-2" do |node2|
    node2.vm.box = "ubuntu/bionic64"
    node2.vm.network "forwarded_port", guest: 8080, host: 8080
    node2.vm.network "forwarded_port", guest: 8443, host: 8443
    node2.vm.network "forwarded_port", guest: 8822, host: 8022
      config.vm.provider "virtualbox" do |v|
        v.memory = 4048
        v.cpus = 4
      end
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end

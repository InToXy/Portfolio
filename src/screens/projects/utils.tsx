import { FaNetworkWired, FaPython, FaCloud, FaShieldAlt } from 'react-icons/fa';
import pentestImg from '../../assets/pentest.jpg';
import dataImg from '../../assets/data.jpeg';
import cloudImg from '../../assets/cloud.jpeg';
import infraImg from '../../assets/hacker-1944688_1920.jpg';

export interface Project {
  name: string;
  description: string;
  img: string;
  stack: JSX.Element[];
  url?: string;
  git?: string;
}

export const comerciaProjects: Project[] = [];

export const customProjects: Project[] = [
  {
    name: "Introduction au Pentesting",
    description: "Apprentissage de differents type de scan de vulnerabilité et utilisation de scripts afin de les exploiters.",
    img: pentestImg,
    stack: [<FaShieldAlt key="shield" />],
  },
  {
    name: "Traitement de données",
    description: "Création d'un code python pour traiter et mettre en forme un fichier CVE du planning de l'année scolaire.",
    img: dataImg,
    stack: [<FaPython key="python" />],
  },
  {
    name: "Réseau informatique Cloud",
    description: "Mise en place d’un réseau informatique Cloud avec la configuration de différents services sur des machines Centos8.",
    img: cloudImg,
    stack: [<FaCloud key="cloud" />],
  },
  {
    name: "Assurer la sécurisation d'un SI",
    description: "Implémentation complète d'une infrastructure réseau de A à Z incluant sa sécurisation.",
    img: infraImg,
    stack: [<FaNetworkWired key="network" />],
  },
];

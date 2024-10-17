
//* <script type="text/javascript" src="{% static 'css/script_js.js' %}"></script>

const links = document.querySelectorAll('.header_ul a');


    links.forEach(link => {
        link.addEventListener('mouseover', () => {
            link.style.color = 'green';
            link.style.fontSize = '20px';

        });

        link.addEventListener('mouseout', () => {
            link.style.color = '';
            link.style.fontSize = ''

        });
    });

const nav1 = document.getElementById('nav1');
    links.forEach(link => {
        link.addEventListener('mouseover', () => {
            nav1.style.transform = 'scale(1.3)';
            nav1.style.transition = 'transform 0.3s ease';
        });

    link.addEventListener('mouseout', () => {
        nav1.style.transform = 'scale(1)';
        });
    });
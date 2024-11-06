document.addEventListener('DOMContentLoaded', () => {
    
    const menuItems = document.querySelectorAll('.nav_panel li');

    menuItems.forEach(item => {
        const dropdown = item.querySelector('.dropdown-menu');

        if (dropdown) {
            item.addEventListener('mouseenter', () => {
                dropdown.style.display = 'block';
                setTimeout(() => {
                    dropdown.style.opacity = '1';
                    dropdown.style.visibility = 'visible';
                    dropdown.style.transform = 'translateY(0)';
                }, 10);
            });

            item.addEventListener('mouseleave', () => {
                dropdown.style.opacity = '0';
                dropdown.style.visibility = 'hidden';
                dropdown.style.transform = 'translateY(-10px)';
                setTimeout(() => {
                    dropdown.style.display = 'none';
                }, 300);
            });
        }
    });

    document.addEventListener('click', (event) => {
        if (!event.target.closest('.nav_panel')) {
            menuItems.forEach(item => {
                const dropdown = item.querySelector('.dropdown-menu');
                if (dropdown) {
                    dropdown.style.opacity = '0';
                    dropdown.style.visibility = 'hidden';
                    dropdown.style.transform = 'translateY(-10px)';
                    setTimeout(() => {
                        dropdown.style.display = 'none';
                    }, 300);
                }
            });
        }
    });

    
    const skillBars = document.querySelectorAll('.skill-bar');

    
    const fillPercentages = [52, 60, 80, 90, 45, 55];

    
    skillBars.forEach((bar) => {
        const barInner = document.createElement('div');
        barInner.classList.add('skill-bar-inner');
        bar.appendChild(barInner);
    });

    
    const img = document.querySelector('.animated-image');
    img.addEventListener('animationend', () => {
        
        skillBars.forEach((bar, index) => {
            const barInner = bar.querySelector('.skill-bar-inner');
            setTimeout(() => {
                barInner.style.width = `${fillPercentages[index]}%`;
            }, index * 500);
        });
    });
});
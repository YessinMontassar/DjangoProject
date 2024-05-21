function getNotifications() {
    fetch('/get-notifications/')
    .then(response => response.json())
    .then(data => {
        const notifications = data.notifications;
        notifications.forEach(notification => {
            // Afficher la notification à l'utilisateur (par exemple, dans une boîte de dialogue ou un élément de liste)
            console.log(notification.message);
        });
    });
}

// Appeler la fonction getNotifications() périodiquement
setInterval(getNotifications, 60000); // Par exemple, appel

function markNotificationsAsRead() {
    fetch('/mark-notifications-as-read/')
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Les notifications ont été marquées comme lues avec succès
        }
    });
}
$('#notificationModalLabel').on('shown.bs.modal', function () {
    // Appeler markNotificationsAsRead() lorsque la fenêtre modale est ouverte
    markNotificationsAsRead();
});
$('#myModal').on('shown.bs.modal', function () {
    $.ajax({
        type: 'GET',
        url: '/get-notifications/', // Remplacez '/get-notifications/' par l'URL de votre vue Django qui renvoie les notifications non lues
        success: function(data) {
            // Supposons que les données retournées sont au format JSON avec une propriété 'notifications'
            const notifications = data.notifications;
            // Afficher les notifications dans la fenêtre modale
            notifications.forEach(notification => {
                $('#notification-list').append(`<p>${notification.message}</p>`);
            });
        },
        error: function(xhr, status, error) {
            console.error('Une erreur s\'est produite lors de la récupération des notifications:', error);
        }
    });
});